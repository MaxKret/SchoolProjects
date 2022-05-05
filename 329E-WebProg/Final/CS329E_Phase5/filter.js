// // Filterable Divs

$(function () {
  $("#All").prop("checked", true);
  $(".filterbtn").click(function () {
    const filterClass = this.value;
    if ($(this).prop("checked") == true) {
      currFilters.push(filterClass);
      if (filterClass !== "store-feature") currFilters.splice(currFilters.indexOf("store-feature"), 1);
    }
    else if ($(this).prop("checked") == false) {
      currFilters.splice(currFilters.indexOf(filterClass), 1);
      if (currFilters.length < 1) currFilters.push("store-feature");
    }
    filterSelection();
  });
  filterSelection();
});

var currFilters = ["store-feature"];
// var filterMap = {"retail": ["boutique"],"food": ["breakfast","subs","alcohol","pizza"]};

function filterSelection() {
  var storeFeaturesArr, idx;
  storeFeaturesArr = document.getElementsByClassName("store-feature");
  for (idx = 0; idx < storeFeaturesArr.length; idx++) {

    // prematurely hide the element
    removeClass(storeFeaturesArr[idx], "show");

    // check if it should be shown
    const currClassStr = storeFeaturesArr[idx].className;
    let elementClassArr = currClassStr.split(' ');
    let filterMatch = false;
    elementClassArr.forEach((classTag) => {
      if (currFilters.includes(classTag)) filterMatch = true;
    });
    if (filterMatch) {
      addClass(storeFeaturesArr[idx], "show");
    }
    // if (filterClass == "store-feature") filterClass = "";

  }
}

// Show filtered elements
function addClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    if (arr1.indexOf(arr2[i]) == -1) {
      element.className += " " + arr2[i];
    }
  }
}

// Hide elements that are not selected
function removeClass(element, name) {
  var i, arr1, arr2;
  arr1 = element.className.split(" ");
  arr2 = name.split(" ");
  for (i = 0; i < arr2.length; i++) {
    while (arr1.indexOf(arr2[i]) > -1) {
      arr1.splice(arr1.indexOf(arr2[i]), 1);
    }
  }
  element.className = arr1.join(" ");
}