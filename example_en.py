#!/usr/bin/env python
# coding: utf-8

import BM25F.core
import BM25F.en
import BM25F.exp

tokenizer = BM25F.en.Tokenizer(token_filter=BM25F.en.TokenFilter())

bj = BM25F.exp.bag_jag()

bd0 = BM25F.exp.bag_dict().read(tokenizer, {
    'title': 'data-for-testing',
    'body': 'tested',
    'anchor': 'Monitors\'',
})
bj.append(bd0)

bd1 = BM25F.exp.bag_dict().read(tokenizer, {
    'title': 'TestData',
    'body': 'Do a test',
})
bj.append(bd1)

bd2 = BM25F.exp.bag_dict().read(tokenizer, {
    'body': 'Test.',
})
bj.append(bd2)

bd3 = BM25F.exp.bag_dict().read(tokenizer, {})
bj.append(bd3)

query = BM25F.exp.bag_of_words().read(tokenizer, 'test monitor')

boost = BM25F.core.param_dict(default=1.0)
boost['title'] = 100
boost['body'] = 0.1

k1 = 2.0

b = BM25F.core.param_dict(default=0.75)
b['title'] = 0.50
b['body'] = 1.00

print(BM25F.core.bm25f(query, bd0, bj, boost=boost, k1=k1, b=b))