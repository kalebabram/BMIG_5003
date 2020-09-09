#!/bin/bash
# Ask the user for their name

IntoCentieter=2.54
LbstoKg=0.453592
echo What is your name?
read x
FirstName="$(echo $x | cut -d' ' -f1)"
LastName="$(echo $x | cut -d' ' -f2)"

echo What is your height in inches?
read heightIn
echo What is your weight in pounds?
read weightLbs
heightCM=`bc <<< "${heightIn}*${IntoCentieter}"`
heightM=`bc <<< "${heightIn}*0.0254"`
heightMsq=`bc <<< "${heightM}*${heightM}"`
weightKg=`bc <<< "${weightLbs}*${LbstoKg}"`
bmi=`bc <<< "${weightKg}/${heightMsq}"`

echo =========================

echo Your first name is: $FirstName
echo You last name is: $LastName

echo Your height in cm is: $heightCM


echo Your weight in kg is: $weightKg
echo Your BMI is: $bmi
