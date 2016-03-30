
This repo is a POC of using Chris Leishman's [`libcypher-parser`](https://github.com/cleishm/libcypher-parser) library from Python using CFFI.

This program displays errors in 2 sample Cypher queries. The queries are:

    MATCH (n) RET n;
    MATCH (n) RETURN n;

**WARNING**: I am not a C expert and my solution is most definitely a hack.

![I have no idea what I am doing](http://img1.rnkr-static.com/user_node_img/50013/1000240969/870/doing-science-photo-u1.jpg)


## Installation

For details, see README for [`libcypher-parser`](https://github.com/cleishm/libcypher-parser).

On Mac OS X, these work for me:

```bash
brew install cleishm/neo4j/libcypher-parser
make
```

You will also need to install `cffi` python library.

To run the program:

```python
python run.py
```

### Notes

Location of [API](https://cleishm.github.io/libcypher-parser/doc/latest/cypher-parser_8h.html)
