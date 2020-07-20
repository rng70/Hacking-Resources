# CTF Resources



`CTF challenges are usually categorized into one of these broad groups, and although at times they may be labeled, it is usually up to the competitor to find out what type of challenge it is. Here are some broad guidelines to finding out what type of challenge is presented:`

* `Is the challenge given as a web link? If following the link does not download a file, the challenge is most likely a` ___`web`___ `one.`

* `Is the file provided an image or music file? If so, the challenge is most likely a` ___`steganography`___ `one.`

* `If the file is a jumbled text file, it is most likely a` ___`cryptography`___ `challenge.`

* `If the file provided is not readily identifiable, the best tool to use is the` ___`file`___ `command, which tells you what type of file it is.`
  * `If the file output is PCAP or relating to packets or the web, the challenge is likely a` ___`web`___ `one.`
  * `If the file output is an ELF file, it is most likely a` ___`reversing`___ `challenge.`
  * `If the file output is an executable, it is most likely a` ___`reversing`___ `challenge.`
  * `Last resort, google the output of the` `file` `command on the file`



## Cryptography



### What is Cryptography?

---

_According to_ __[`Wikipedia`](http://en.wikipedia.org/wiki/Cryptography "http://en.wikipedia.org/wiki/Cryptography")__

> __Cryptography is the practice and study of techniques for secure communication in the presence of third parties__

In the case of CTF’s, the goal is to crack or clone cryptographic objects or algorithms to reach the flag.



### Common To Start

---

To decrypt a message or text or some flags it is common to use some available method to crack the hash and some of them are included here:

1. If the text is 32 characters long then probably it is an ***`md5`*** hash
2. If the text is 40 characters long the probably it is a ***`SHA1`*** hash
3. If the text only contains letters not numbers or special characters then probably it is a ***`Caesar`*** or ***`Vigenere`*** type hash
4. If `=` signs are spread out the text then probably it is a ***`base64`*** hashed string
5. Most interestingly, it is rare but not uncommon to have a ***`KeyBoard Map`*** introduced in [Olympic CTF 2014](https://github.com/ctfs/write-ups/tree/master/olympic-ctf-2014/crypting)
6. If any hints is available about keys or signing then most probably it is an ***`RSA`***



#### [md5 Hashing](https://en.wikipedia.org/wiki/Md5)

---

md5 is a hashing function which creates a 16-byte hash value (usually represented as a 32 digit hexadecimal number) from any file.

##### Tools and Use

* Create Hash:
  * Online [here](http://www.md5-creator.com/)
  * The [md5sum](https://en.wikipedia.org/wiki/Md5sum) command line program
* Decrypt Hash:
  * Online [here](http://www.md5decrypter.co.uk/)

##### See More

* 



#### [SHA1 Hashing](https://en.wikipedia.org/wiki/Sha1)

---

SHA1 is a hash function which creates a 20-byte hash value (usually represented by a 40 digit hexadecimal number) from any file.

##### Tools and Use

* Create Hash:
  * Online [here](http://ratfactor.com/sha1)
  * The [sha1sum](https://en.wikipedia.org/wiki/Sha1sum) command line program
* Decrypt Hash:
  * Online [here](http://www.stringfunction.com/sha1-decrypter.html)

##### See More

* 



#### [Caesar Cipher](https://en.wikipedia.org/wiki/Caesar_cipher)

---

The Caesar Cipher is a very simple and common encryption method which shifts a string of letters a certain number of positions up or down the alphabet.

##### Tools and Use

* Create Hash:
  * Online [here](http://tools.zenverse.net/caesar-cipher/)
  * [Python script](http://www.stealthcopter.com/blog/2009/12/python-cryptography-caesar-shift-encryption-shift-cipher/)
* Decrypt Hash:
  * Online [here](http://tools.zenverse.net/caesar-cipher/)
  * [Bash script](http://www.linux-support.com/cms/chris-lamb-decrypting-the-caesar-cipher-using-shell/)

##### See More

* 



#### Vigenère Cipher

---

The Vigenère Cipher is an encrypting method which uses a series of different Caesar ciphers based on the letters of a keyword. It was first developed in the mid-16th century, and has ever since been popular in the cryptography and code-breaking community. It was considered unbreakable until 1863, when Friedrich Kasiski published the first successful generic attack method of the cipher (although Charles Babbage probably managed to break it earlier, but didn't explain his method).

Several variants of the Vigenère Cipher exists, for example the Beaufort Cipher and the Gronsfeld Cipher. More recent ciphers, like the Enigma or the M-209 cipher machine, were also built on the same principles (polyalphabetic substitution ciphers).

##### Tools and Use

* Create Hash:
  * Online [here](http://sharkysoft.com/vigenere/)
* Decrypt Hash:

  * Online [here](http://smurfoncrack.com/pygenere/index.php)

##### See More

* [Boxentriq](https://www.boxentriq.com/code-breaking/vigenere-cipher) - easy to use cracker and information about Vigenère Cipher (including variants such as Beaufort, Gronsfeld)
* [Online Vigenère cracker](http://www.mygeocachingprofile.com/codebreaker.vigenerecipher.aspx)



#### [Base64 Encoding](https://en.wikipedia.org/wiki/Base64)

---

Base64 encoding is a way to represent binary data as text.

##### Tools and Use

* Encode:

  * The [base64](http://linux.die.net/man/1/base64) command line program

* Decode:

  * Online [here](http://www.base64decode.org/)
  * The [base64](http://linux.die.net/man/1/base64) command line program

##### See More

* 



#### [RSA](https://en.wikipedia.org/wiki/RSA_algorithm)

---

RSA is a public-key cryptosystem which uses a public-private key pair to encrypt and decrypt information securely.

##### Tools and Use

* RSA library in [python](https://pypi.python.org/pypi/rsa) with easy to use [docs](http://stuvel.eu/files/python-rsa-doc/usage.html)
* [Thorough explanation](http://www.muppetlabs.com/~breadbox/txt/rsa.html) of RSA with a [simple crack example](http://www.muppetlabs.com/~breadbox/txt/rsa.html#13)

##### See More

* 

### See More

---

[Introduction to Cryptography](http://www.cs.umd.edu/~waa/414-F11/IntroToCrypto.pdf)



## [Steganography](http://en.wikipedia.org/wiki/Steganography)



### What is Steganography?

---

Steganography involves concealing a message, image, or file within another message, image, or file.

In the context of CTFs steganography usually involves finding the hints or flags that have been hidden with steganography.  Most commonly a media file will be given as a task with no further instructions, and the participants have to be able to uncover the message that has been encoded in the media.



### Common To Start

---

* If the file is an image, see [File in an Image](./ctf_resources.md#File%20in%20an%20Image)
* If the file is an text-file, see [Text Hidden in Text/Image](./ctf_resources.md#Text Hidden in Text/Image)



#### Hidden Fine in an Image

---

One of the most common steganography tricks is to hide a file inside of an image.  The file will open normally as an image but will also hold hidden files inside, commonly zip, text, and even other image files.

The reason this works is because when an image file is read it has starting and ending bytes dictating the size of the image.  The image viewer that you use will use the information between these bytes to present an image to you, ignoring anything after the terminating byte.

For example, The terminating byte for a `JPEG` is `FF D9` in hex, so using a hex viewer ([xxd](http://linuxcommand.org/man_pages/xxd1.html) is good for Linux, or something like [HxD](http://mh-nexus.de/en/hxd/) for windows) you can find out where the image finishes.  These bytes are sometimes hard to find in a sea of numbers though, so looking at the dump of the hex (the text representing the hex bytes) can also help you find hidden .txt or .zip files.

Solve [ctfexample.jpg](./File-in-Image/ctfexample.jpg) and [example.jpg](./File-in-Image/example.jpg)

##### Example

---

A very simple implementation of this strategy is used in the [example.jpg](./File-in-Image/example.jpg) file in this directory. If you save it to your computer and open it up with an image viewer, you should be presented with a simple jpg image.

Now lets try to find the flag. Open up the image in your favorite hex editor and start looking around for something odd (You may find the flag itself from the dump at this point, but for the sake of example try extracting it). Near the bottom of the file you should see the terminating byte of a jpg `ffd9`:

`01e17a0: 685c 7fab 8eb4 5b32 61f1 c4ff d950 4b03  h\....[2a....PK.`

Another important part of this line is the `PK` near the end. `PK` are the initials of Phil Katz, the inventor of the zip file, and indicate that a zip file starts at that point.

Using this information we can use another handy Linux tool, [`dd`](http://en.wikipedia.org/wiki/Dd_(Unix)). The `dd` command is very versatile and allows for the copying and converting of a multitude of files. In our case, we are going to be using it to extract the zip file.

We know where the location of the zip file is, but `dd` only takes decimal values, so we convert the hexadecimal location 0x01e17ad from hex to decimal to get 1972141.

Plugging this into `dd`:

`dd if=example.jpg bs=1 skip=1972141 of=foo.zip`

This takes in the image example.jpg, the 'in file' if, reads one block at a time, 'block size' bs,  skips to block 1972141, skip,  and writes it to the 'out file' zip we call foo.zip. When this completes you should have a zip file you can easily unzip to access the text file inside.

This is the long way of solving a simple steganography problem but shows how the strategy works. In the Solving section more concise and efficient methods are described.



##### Detecting

---

These challenges are usually presented as a simple picture with no other instructions, and it is up to the competitor to run it through a hex editor to find out if it involves steganography.  If you are presented with an image and no instructions, your safest bet is that is has something hidden after the closing tags of the image.



##### Solving

---

Although it is possible and at times practical to solve these tasks using Linux tools like `dd`, there are some tools that make it much easier. [`Binwalk`](http://binwalk.org/) is an immensely useful tool which automatically detects and extracts files hidden with steganography tools.



##### CTF Example

---

Steganography of this type is usually not scored very highly but is decently widespread. Back-Door-CTF 2014 created one which is generally straightforward,  [ctfexample.jpg](./File-in-Image/ctfexample.jpg), but involves multiple layers.



##### See More

---

* [XXD](http://linuxcommand.org/man_pages/xxd1.html)
* [HxD](http://mh-nexus.de/en/hxd/)
* [DD](https://en.wikipedia.org/wiki/Dd_%28Unix%29)
* [Binwalk](http://binwalk.org/)



#### Text Hidden in Text/Image

----

Text can be hidden by making it nearly invisible (turning down it's opacity to below 5%) or using certain colors and filters on it.  Although the text is indiscernible to the naked eye, it is still there, and there are a variety of tools which allow the text to be extracted.

Solve [ctf-example.png](./Invisible-Text/ctf-example.png) and [example.png](./Invisible-Text/example.png)

##### Tools and Use

---

* Create

  * Watermark example [in GIMP](http://www.wikihow.com/Create-Hidden-Watermarks-in-GIMP)

* Find

  * [GIMP](http://www.gimp.org/) or [Photoshop](http://www.photoshop.com/) can be used to uncover the flag by using different filters and color ranges, as shown in the same [watermark guide](http://www.wikihow.com/Create-Hidden-Watermarks-in-GIMP) as above.

  * [Stegsolve](https://www.wechall.net/forum/show/thread/527/Stegsolve_1.3/page-1) is an immensely useful program for many steganography challenges, allowing you to go through dozens of filters to try to uncover hidden text.

  * There are many scripts that have been written to substitute certain colors and make hidden the text legible, for example [this](http://pastebin.com/46VmzrRU) Ruby script highlights colors passed to it in the image.



## Reverse Engineering

Reversing in the context of CTFs is usually the reverse engineering of software (executables/bin files) into assembly code and at times the original source code to understand what is happening in a program, break a program (buffer overflows), or to decrypt encryptions done by a program. Challenges related to reversing are usually not as easy to pick up on as others, and require a lot of diligence and learning to truly understand and be able to tackle.

### Books & Tools

---

* Book
  * [Reverse Engineering for Beginners](https://github.com/dennis714/RE-for-beginners) - an extremely well-written and verbose free book which explains multiple CPU instruction sets and methods for writing and understanding them.
* Tool
  * gdb: Basic debugger (+gef/peda)
  * objdump: Very basic disassembler
  * ghidra: Sophisticated disassembler that can also [Decompile Code](https://ghidra-sre.org/)



## Web Scripting

Web challenges in CTF competitions usually involve the use of HTTP (or similar protocols) and technologies involved in information transfer and display over the internet like PHP, CMS's ( .i.e Django), SQL, JavaScript, and more.  There are many tools used to access and interact with the web tasks, and choosing the right one is a major facet of the challenges. Although web browsers are the most common and well known way of interacting with the internet, tools like `curl` and `nc` allow for extra options and parameters to be passed and utilized.



### Common To Start

---

Login field/text input a central part of website? Two major possible options:

* If a database is involved, likely a [SQL injection](./sql-injections/)
* If the input is used in the website, possible [XSS vulnerability](./xss/)



#### [SQL Injection](https://en.wikipedia.org/wiki/SQL_injection)

---

* Learn
  * Good [introduction and database](https://www.owasp.org/index.php/SQL_injection) of SQL injections



#### [XSS vulnerability](https://en.wikipedia.org/wiki/Cross-site_scripting)

---

Cross-site scripting (XSS) is a typical web vulnerability which allows attackers to inject their own client-side code into the website.



##### Resource

---

* Learn
  * Introduction by [Google](https://www.google.com/about/appsecurity/learning/xss/index.html) to the topic
  * Game by [Google](https://xss-game.appspot.com/) for fun and practice



## Binary Exploitation



### [Buffer Overflow](https://en.wikipedia.org/wiki/Buffer_overflow)

---

A buffer overflow occurs when a buffer (i.e., an array) is filled with more data than it can hold. The excess bytes of data are written directly into memory, often causing a [segfault](https://en.wikipedia.org/wiki/Segmentation_fault) and crashing the program.

Vulnerable programs can be explioted to redirect the instruction pointer to point to malicious code or [shell code](https://en.wikipedia.org/wiki/Shellcode).

Buffer overflows are common in compiled langauges like C and C++, where array boundaries are not checked.



#### Vulnerable Functions

---

The table below shows several C and C++ functions vulnerable to buffer overflows and their safe alternative:

| Vulnerable | Safe     |
| ---------- | -------- |
| strcpy     | strncpy  |
| strcat     | strncat  |
| sprintf    | snprintf |
| gets       | fgets    |



#### Real World Examples

---

Real world examples of buffer overflow exploits:

- [Morris Worm](https://en.wikipedia.org/wiki/Morris_worm)
- [Code Red Worm](https://en.wikipedia.org/wiki/Code_Red_worm)
- [Twilight Princess Exploit](https://en.wikipedia.org/wiki/The_Legend_of_Zelda:_Twilight_Princess#Technical_issues)



#### See More

---

* [CTF 101 - Binary Exploitation](https://ctf101.org/binary-exploitation/buffer-overflow/)