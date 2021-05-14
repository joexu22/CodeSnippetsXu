㊌㊌㊌ ㊎㊎㊎
By: Joe Xu
Title: StakeFish Questions
㊌㊌㊌ ㊎㊎㊎


1. How often does the Bitcoin network see two consecutive blocks mined more than 2 hours apart from each other?
We'd like to know your answer (it doesn't have to be precise) and your approach towards this solution using probability and statistics.

Through researching this problem, various concept came about:
  - Block Time: in the context of cryptocurrencies, is a measure of the time it takes to produce a new block
  - Difficulty: is a parameter that cryptocurrencies use to keep the average time between blocks steady as the network's hash power changes

On How Difficulty is Calculated
  - Difficulty changes every 2016 blocks -
    - 14days * 24hours * 6BlockTime = 2016
	- This 2016 number is important because it is how many 10minute blocks there are in 2 weeks

  - difficulty = difficulty_1_target / current_target
	-  => current_target = difficulty_1_target / difficulty
       -  where difficulty_1_target is "old_difficulty * 2weeks"
       -  where difficulty is "time the past 2015 blocks took"

On an actual statistical equation involving probability distributions:
  - This is an "actual" solution...
  - [Actually Solution?](./statistic.ipynb)

Citations:

* Bitcoin. "Bitcoin: A Peer-to-Peer Electronic Cash System", http://bitcoin.org/bitcoin.pdf
* Bitcoin. "Vocabulary", https://bitcoin.org/en/vocabulary
* BitcoinWiki. "Difficulty in Mining", "https://en.bitcoinwiki.org/wiki/Difficulty_in_Mining
* Blockchain.com. "Blockchain Explorer", https://www.blockchain.com/explorer/
* BTC.com "Bitcoin Block Explorer", https://btc.com/
* data.bitcoinity.org "Average time to min a block in minutes", https://data.bitcoinity.org/bitcoin/block_time/5y?f=m10&t=l
* DeathAndTaxes. "Why was the target block time chosen to be 10 minutes?", https://bitcoin.stackexchange.com/a/1864
* O'Reilly Media, Inc. "Mastering Bitcoin", https://www.oreilly.com/library/view/mastering-bitcoin/9781491902639/ch08.html
* YCharts. "Bitcoin Blockchain Size", https://ycharts.com/indicators/bitcoin_blockchain_size
* 손동하, "Bitcoin#6: Target and Difficulty", https://medium.com/@dongha.sohn/bitcoin-6-target-and-difficulty-ee3bc9cc5962

-----

2. How many times the above had happened so far in the history of Bitcoin?
You can use any mainstream programming language to retrieve the answer and provide us the codes.

I went for a data scraping approach - where I gather all the timestamps and count how many are 2 hours apart

Here are the steps I took to solve this problem:

I was able to run a "Full Bitcoin Node"/Validator using AWS
  - did not want to use up ~400GB worth of bandwidth
  - things should be more or less synced to save on download time
  - what I really need was the blk*.dat files

Was able to find a suitable image
  - * https://aws.amazon.com/marketplace/pp/B07W3V6K85

The AWS Image was mostly configured pretty well
  - Most instructions are here
  	- http://www.techlatest.net/support/bitcoin_fullnode_support/
  - Access the Remove Images
    - use the AWS Console to figure out the Public IP
	- SSH available
	- Windows Remote Desktop also available

Bitcoin Core
  - The image already has Bitcoin Core RPC client version v0.18.0 installed (bitcoin-cli/bitcoin-qt)
  - I was able to download and untar 0.21.1
	- https://bitcoincore.org/en/download/
	- ./bitcoin-0.21.1/bin works and auto detects the existing configs with the blk*.dat
	- Takes a hour or two to sync everything (I'm using a U.S. East Virginia Image upload/download was 800MB when I tested)

Then I looked for a BitCoin parser (found a number of them) (mostly looking for Python Stuff)
  - https://github.com/citp/BlockSci (PYTHON)
  - https://github.com/neldredge/bitcoin-blocks (PERL)
  - https://github.com/ragestack/blockchain-parser (PYTHON)
  - https://github.com/znort987/blockparser (C++)
  - https://github.com/znort987/blockparser (PYTHON)
  - https://vlkan.com/blog/post/2014/06/27/parse-bitcoin-blockchain/ (JAVA)

The easiest one to set up looked like [blockchain-parser](https://github.com/ragestack/blockchain-parser)
  - I tested it on some samples e.g. "blk00000.dat" - "blk00005.dat"
  - seems to work fine for my purposes
  - I noticed that there is a Time Stamp value in Unix Hex Time

The most straightforward solution is to do a linear parse on the data and track the Hex Time
  - I calculate a difference of 7200 seconds (2 hours)
  - if greater, I count it...
  - I inject this logic into the parser
  - Run the code over 2 days
    - (TODO: cut down unnecessary logic)
    - (There is a ton of operations that are superfluous for this task)
	- It happens that the current code write a single text file for each blk*.dat
	  - I repurposed this file to output {current stack height}, {2 hour count}
      - I did "accidentally" stop the run during my testing
	  - I figured that I could recover if the program died form this

			for i in fList:
				 if fList in AlreadyProcessed(lastBlkProcessed):
				 	pass

I got the number up to most recently synced time
  - (did not want to keep bitcoin-core running all the time/network charges?)
  - in the [parsed_data_answer](https://github.com/joexu22/CodeSnippetsXu/tree/master/BLOCKCHAIN/parsed_data_answer) folder each file contains a "checkout" that contains 2 values.
	- these values X, Y mean "up to X stack, Y blocks are timestamped 2 hours apart"

Here is the Empirical Findings:
```
Up to Stack 683310,
163693 blocks where timestamped hours apart
```

Conclusions:
  - I'm actually somewhat surprised at these results, I would of expected a much lesser number
  - At first I suspected a code error or misunderstanding of what timestamp means, but have a stack number of 683310 as of Early March 2021 reassures me that I not too far off the mark (in that every block I am parsing does indeed have one timestamp)
  	- I suspect I am missing the connection between mining and validation
	- Also, I still need to figure out what the "revision" files in the bitcoin-core folder do and how it may be affecting the final tally
  - Ideally, I would need to confirm my findings and methodology 😉

As a Follow-up:
  - Having done this project. I think a natural follow up would be to actually parse out all the data.
  - Created a "Normalized" database table of the Bitcoin Blockchain with some metadata tagging to support faster queries
  - Load all of this into a speedy database
  - Write some queries for insight/lookup
  - Create some APIs for those queries
  - Specially write the API for: ``` What is the count of blocks mined <X> seconds apart? ``` 😉
  