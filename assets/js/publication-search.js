(function () {
  "use strict";
  var zh = /^zh/i.test(document.documentElement.lang || "");
  var root = document.getElementById("publication-results");
  if (!root) return;
  var search = root.querySelector(".publication-search");
  var input = document.getElementById("publication-query");
  var clear = document.getElementById("publication-search-clear");
  var status = document.getElementById("publication-search-status");
  var empty = document.getElementById("publication-search-empty");
  var groups = [];
  var papers = [];
  var group;
  Array.prototype.forEach.call(root.children, function (element) {
    if (element.classList.contains("publication-year")) {
      group = { heading: element, papers: [] };
      groups.push(group);
    } else if (element.classList.contains("paper-box")) {
      var text = (group ? group.heading.textContent + " " : "") + element.textContent;
      var paper = { element: element, text: text.toLowerCase().replace(/\s+/g, " ") };
      papers.push(paper);
      if (group) group.papers.push(paper);
    }
  });
  function removeHighlights(element) {
    Array.prototype.forEach.call(element.querySelectorAll("mark.search-match"), function (mark) {
      mark.parentNode.replaceChild(document.createTextNode(mark.textContent), mark);
    });
    element.normalize();
  }
  function highlight(element, terms) {
    if (!terms.length) return;
    var walker = document.createTreeWalker(element, NodeFilter.SHOW_TEXT, {
      acceptNode: function (node) {
        return node.parentElement.closest("script, style, mark") ? NodeFilter.FILTER_REJECT : NodeFilter.FILTER_ACCEPT;
      }
    });
    var nodes = [];
    while (walker.nextNode()) nodes.push(walker.currentNode);
    nodes.forEach(function (node) {
      var text = node.nodeValue;
      var lower = text.toLowerCase();
      var ranges = [];
      terms.forEach(function (term) {
        var start = lower.indexOf(term);
        while (start !== -1) {
          ranges.push([start, start + term.length]);
          start = lower.indexOf(term, start + 1);
        }
      });
      if (!ranges.length) return;
      ranges.sort(function (a, b) { return a[0] - b[0]; });
      var merged = [];
      ranges.forEach(function (range) {
        var last = merged[merged.length - 1];
        if (last && range[0] <= last[1]) last[1] = Math.max(last[1], range[1]);
        else merged.push(range.slice());
      });
      var fragment = document.createDocumentFragment();
      var cursor = 0;
      merged.forEach(function (range) {
        fragment.appendChild(document.createTextNode(text.slice(cursor, range[0])));
        var mark = document.createElement("mark");
        mark.className = "search-match";
        mark.textContent = text.slice(range[0], range[1]);
        fragment.appendChild(mark);
        cursor = range[1];
      });
      fragment.appendChild(document.createTextNode(text.slice(cursor)));
      node.parentNode.replaceChild(fragment, node);
    });
  }
  function filter() {
    var query = input.value.trim().toLowerCase();
    var terms = query.split(/\s+/).filter(Boolean);
    var count = 0;
    removeHighlights(root);
    papers.forEach(function (paper) {
      var matches = terms.every(function (term) { return paper.text.indexOf(term) !== -1; });
      paper.element.hidden = !matches;
      if (matches) {
        count++;
        highlight(paper.element, terms);
      }
    });
    groups.forEach(function (group) {
      group.heading.hidden = !group.papers.some(function (paper) { return !paper.element.hidden; });
      if (!group.heading.hidden) highlight(group.heading, terms);
    });
    status.textContent = query
      ? (zh ? count + " / " + papers.length + " 篇论文" : count + " of " + papers.length + " publications")
      : (zh ? papers.length + " 篇论文" : papers.length + " publications");
    clear.hidden = input.value.length === 0;
    empty.hidden = count !== 0;
  }
  input.addEventListener("input", filter);
  clear.addEventListener("click", function () {
    input.value = "";
    filter();
    input.focus();
  });
  input.addEventListener("keydown", function (event) {
    if (event.key === "Escape") {
      input.value = "";
      filter();
    }
  });
  search.hidden = false;
  filter();
})();
