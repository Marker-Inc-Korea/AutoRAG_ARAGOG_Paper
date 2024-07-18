# AutoRAG_ARAGOG_Paper

# Installation

```bash
pip install -r requirements.txt
```

# Running the project

1. Make `.env` file using `.env.template` file.
2. Run evaluator with the following command.
```bash
python run.py
```
3. Check the result in the result folder.

You can check the example config file at config folder.

And you can specify qa data path, corpus data path, and project dir if you want.


# ⚠️ Warning ⚠️
The use of RAGAS Context Precision to score retrievals is very expensive, so it is currently removed from AutoRAG. 
The repo specifies in the requirement.txt that AutoRAG version 0.1.12 should be able to use RAGAS Context Precision.
However, it can be expensive to test, so be careful when using it.
