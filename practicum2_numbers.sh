#!/bin/bash

read -p "Enter numberical list separated by 'space' : " input

function Scrub() {
    InitialList=$(echo $input | tr " " "\n")
}

function Sort() {
    SortedList=$(echo $input | tr " " "\n" | sort -nu)
}

function Resort() {
    ResortedList=$(echo $input | tr " " "\n" | sort -rnu)
}
Scrub
Sort
Resort

case $InitialList in
    $SortedList)
        echo Your list is ascending
        ;;
    $ResortedList)
        echo Your list is descending
        ;;
    *)
        echo Your list is unsorted
        ;;
esac
