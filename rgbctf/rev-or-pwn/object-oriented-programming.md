# Object Oriented Programming

So, the source is less obfuscated and more elongated. It's got a lot of bloat, but let's focus on the important things.

1. We've got a bunch of classes. Each class has a two letter name, and has a bunch of two letter name functions. Each of these functions returns a 2 letter string.
2. These essentially form a lookup table, pair of chars + pair of chars = another pair of chars
3. Our input is gotten, then the function executeCodeThatDoesSomethingThatYouProbablyNeedToFigureOut is run on the input. The output is compared to scanner.getClass\(\).getPackageName\(\).replace\(".", ""\) scanner.getClass\(\).getPackageName\(\).replace\(".", ""\) = javautil This means our target output is javautil.

Let's look at the actual function.

```javascript
    public static String executeCodeThatDoesSomethingThatYouProbablyNeedToFigureOut(String stringToExecuteAforementionedCodeOn) throws Exception {
        String encryptedString = reallyBasicQuoteUnquoteEncryptionFunctionThatWillOnlyTakeTimeToFigureOutIfYouKeepReadingTheseRidiculouslyLongMethodNames(stringToExecuteAforementionedCodeOn);
        String returnValueOfThisFunction = new String();
        String[] chunksOfEncryptedStringOfLengthFour = splitStringIntoChunksOfLength(encryptedString, FOUR);
        for (String chunkOfEncryptedStringOfLengthFour : chunksOfEncryptedStringOfLengthFour) {
            String[] chunksOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = splitStringIntoChunksOfLength(chunkOfEncryptedStringOfLengthFour, TWO);
            String firstChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = chunksOfChunkOfEncryptedStringOfLengthFourOfLengthTwo[0];
            String secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = chunksOfChunkOfEncryptedStringOfLengthFourOfLengthTwo[1];
            Class<?> classAndExtraCharactersSoItsNotAKeyword = Class.forName(firstChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo);
            Object object = classAndExtraCharactersSoItsNotAKeyword.getConstructors()[ZERO].newInstance();
            for (int loopArbitraryCounterIterator = 0; loopArbitraryCounterIterator < THREE; loopArbitraryCounterIterator++) {
                Method method = classAndExtraCharactersSoItsNotAKeyword.getMethod(secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo);
                secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo = (String)method.invoke(object);
            }
            returnValueOfThisFunction = new String(returnValueOfThisFunction + secondChunkOfChunkOfEncryptedStringOfLengthFourOfLengthTwo);
        }
        return returnValueOfThisFunction;
    }
```

Bloated, I know, but we can split the logic up. It splits the input into chunks of 4. It iterates over these chunks of 4. For every chunk of 4, it splits it into 2 chunks of 2. NOTE: this is all done on the input after the "encryption" 1. Grab the class name associated with the first chunk of 2 2. Iterate to do this three times: a. Grab method of class that chunk 2 corresponds to. b. call function, set chunk 2 to the output 3. Append the final chunk 2 to the output So, say we sent kpta It would go to class kp, and search for a method called ta. It would call ta, then store the output, and try to find the method corresponding to this output... etc. etc. This means we want the first chunk of 4 to result in ja, the second to result in va, the third ut, the fourth il.

This means we will want to find a chain of functions within 4 classes. The chain would have

function that returns name of function that returns name of function that returns name of function that returns string we want

We can search manually for these chains.

```text
gl.java vg -> we -> rb -> ja
pr.java pk -> te -> wj -> va
qg.java am -> xs-> mb-> ut
fg.java gg-> mg-> oa-> il
```

So, the input, after the encryption is done, must be \[class name\]\[start of chain\]\[class name\]\[start of chain\]

This means our input, when encrypted, must be `glvgprpkqgamfggg`

If we look carefully at the encryption, we find it's actually just an XOR. Now, you know XOR, encryption and decryption are the same operation. So we can just run the encryption function on `glvgprpkqgamfggg` to get the flag, `enterprisecodeee`

## Flag: rgbCTF{enterprisecodeee}

