# Automated key-finding with IDA python script

This is a simple IDA python script that can be used to find the key for executable file `bobby.exe`.

## Getting started

### Overview

* Reversing the binary is the main task.
* Find out how the input string is compared with the key.
* Understand the flow to intentionally reverse-compute the correct key.
* Run script in IDA pro.

### Program Flow

```txt
1. Set breakpoint.
2. Extract register values at that point.
3. Reverse-compute the correct key string from the algorithm.
```

## Running the program

### Build

It's a script. Just run it in IDA pro.

### Run

Just `Run script` in IDA pro.

## Authors

* **James Sung** - *Initial work* - [sjkywalker](https://github.com/sjkywalker)
* Copyright © 2018 James Sung. All rights reserved.
