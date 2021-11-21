#!/bin/sh
touch fake.txt fake1.txt result.txt

echo "fake file content" > fake.txt
echo checking input
./lab0 --input fake.txt > result.txt

echo checking output
./lab0 --input fake.txt --output fake1.txt 
cat fake1.txt >> result.txt

echo checking options handling
./lab0 --input 2>> result.txt
./lab0 --fakeopt 2>> result.txt

echo check segfault
./lab0 --segfault 2>> result.txt
./lab0 --catch --segfault 2>> result.txt
echo check dump-core
./lab0 --catch --segfault --dump-core 2>> result.txt

echo "" >> result.txt

VAR=$(diff correct.txt result.txt)

if [ "$VAR" != "" ]; then
	echo incorrect result... sanity check failed
else 
	echo correct result... sanity check passed
fi 

rm -f fake.txt fake1.txt result.txt 
