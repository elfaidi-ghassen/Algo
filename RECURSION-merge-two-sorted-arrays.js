var mergeTwoLists = function(list1, list2) {
    if (list1.length === 0) return list2
    else if (list2.length === 0) return list1
    else {
        if (list1[0] === list2[0]) {
            return [list1[0], list2[0], ...mergeTwoLists(list1.slice(1), list2.slice(1))]
        } else if (list1[0] < list2[0]) {
            return [list1[0], ...mergeTwoLists(list1.slice(1), list2)]
        } else {
          return [list2[0], ...mergeTwoLists(list1, list2.slice(1))]
        }
    }
};

console.log(mergeTwoLists([1, 2, 4], [1, 3, 4]))
