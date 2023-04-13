# Learning Mechanistic Interpretability on Transformers with EasyTransformer (now TransformerLens)


_by Brian Muhia_

Fahamu, Inc


This repository houses the beginnings of a tutorial on mechanistic interpretability for Transformer language models.

#### Pedagogy
So far, we have:
1. Published a usable visualiser for tokens, fashioned from the `Hacky Interactive Lexoscope` by Neel Nanda.
1. Written notes from rewriting `EasyTransformer_Demo.ipynb` by Neel, in order to learn the library and how to use it.

#### Output
1. Applied some tools and ideas in the demo towards observing induction heads in [`SOLU-8l-old`](https://transformer-circuits.pub/2022/solu/index.html), also trained by Neel.
1. Generated IOI-style datasets:
    - pkl_ioi_data.pkl is 100000 rows of IOI sentences from `ABBA` templates, most of which use multi-token terms.
    - https://huggingface.co/datasets/fahamu/ioi
        + mecha_ioi_26m.parquet is 26,010,000 rows of IOI sentences, mixing ABBA and BABA templates
        + mecha_ioi_200k.parquet is 200,000 rows of IOI sentences, mixing ABBA and BABA templates

All inspired by the paper _Interpretability in the Wild: a Circuit for Indirect Object Identification in GPT-2 small_, from Redwood Research. We are not affiliated with Redwood Research, and release this dataset to contribute to the collective research effort behind understanding how Transformer language models perform this task. 

###### With thanks and Acknowledgements:

- Esben Kran, Sabrina Zaki - for hosting the Interpretability Jam, which accelerated this work.
- Neel Nanda - for publishing TransformerLens and making public his research process. Wonderful gifts!
