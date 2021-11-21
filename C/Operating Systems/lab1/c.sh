
#!/bin/bash

# UCLA CS 111 Lab 1a testing script, written by Zhaoxing Bu (zbu@ucla.edu).
# This script should only be used when Zhaoxing is in the TA team for 111.

# DO NOT UPLOAD THIS SCRIPT TO WEB OR ANYWHERE ELSE. Any usage without permission
# is strictly forbidden.

# To reader: please read the entire script carefully.

# No partial credits.
# Do not run multiple testing scripts at the same time.
# Only run this on lnxsrv09.seas.ucla.edu please.
# REMEMBER to execute PATH=/usr/local/cs/bin:$PATH in shell to call the correct
# gcc for compiling students' work.
# This PATH change is restored after logging out.
# This script automatically changes the PATH value for you.
# Any comments, suggestions, problem reports are greatly welcomed.

# How to run the script? Place it with students' submissions in the same directory,
# run "./lab1a_sanity_script.sh UID", for example ./lab1a_sanity_script.sh 197705251.

if [ "${PATH:0:16}" == "/usr/local/cs/bin" ]
then
  true
else
  PATH=/usr/local/cs/bin:$PATH
fi

echo "DO NOT run multiple testing scripts at the same time."
echo "Please check if there is any error message below."
echo "==="

# Check tarball.
STUDENT_UID="$1"
SUBMISSION="lab1-$STUDENT_UID.tar.gz"
if [ -e "$SUBMISSION" ]
then
  true
else
  echo "No submission: lab1-$STUDENT_UID.tar.gz"
	exit 1
fi

# Untar into student's directory.
rm -rf $STUDENT_UID
mkdir $STUDENT_UID
tar -C $STUDENT_UID -zxvf $SUBMISSION
cd $STUDENT_UID

# Make.
if [ -e "simpsh" ]
then
  rm -rf simpsh
fi
make || exit

make check
if [ $? == 0 ]
then
  echo "===>make check passed"
else
  echo "===>make check failed"
fi

rm -rf $SUBMISSION
make dist
if [ -e "$SUBMISSION" ]
then
  echo "===>make dist passed"
else
  echo "===>make dist failed"
fi

# Create testing directory.
TEMPDIR="lab1areadergradingtempdir"
rm -rf $TEMPDIR
mkdir $TEMPDIR
if [ "$(ls -A $TEMPDIR 2> /dev/null)" == "" ]
then
  true
else
  echo "Fatal error! The testing directory is not empty."
  exit 1
fi
mv simpsh ./$TEMPDIR/
cd $TEMPDIR

# Create testing files.
cat > a0.txt <<'EOF'
Hello world! CS 111! Knowledge crowns those who seek her.
EOF
cat a0.txt > a1.txt
cat a0.txt > a2.txt
cat a0.txt > a3.txt
cat a0.txt > a4.txt
cat a0.txt > a5.txt
cat a0.txt > a6.txt
cat a0.txt > a7.txt
cat a0.txt > a8.txt
cat a0.txt > a9.txt
cat a0.txt > a10.txt

echo "==="

# Test cases.
echo "Starting grading:"
NUM_PASSED=0
NUM_FAILED=0
# In Lab 1a, --rdonly, --wronly, --command, and --verbose.

# Test case 1 no option.
echo ""
echo "--->test case 1:"
./simpsh >c1out.txt 2>&1
if [ $? == 0 ] && [ ! -s c1out.txt ]
then
  NUM_PASSED=`expr $NUM_PASSED + 1`
  echo "===>test case 1 passed"
else
  NUM_FAILED=`expr $NUM_FAILED + 1`
  echo "===>test case 1 failed"
fi

# Test case 2 bogus option.
echo ""
echo "--->test case 2:"
./simpsh --bogus >c2out.txt 2>c2err.txt
if [ $? == 1 ] && [ ! -s c2out.txt ] && [ -s c2err.txt ]
then
  NUM_PASSED=`expr $NUM_PASSED + 1`
  echo "===>test case 2 passed"
else
  NUM_FAILED=`expr $NUM_FAILED + 1`
  echo "===>test case 2 failed"
fi

# Test case 3 --rdonly can be called with no error.
echo ""
echo "--->test case 3:"
./simpsh --rdonly a1.txt >c3out.txt 2>&1
if [ $? == 0 ] && [ ! -s c3out.txt ] && cmp -s a0.txt a1.txt
then
  NUM_PASSED=`expr $NUM_PASSED + 1`
  echo "===>test case 3 passed"
else
  NUM_FAILED=`expr $NUM_FAILED + 1`
  echo "===>test case 3 failed"
fi
