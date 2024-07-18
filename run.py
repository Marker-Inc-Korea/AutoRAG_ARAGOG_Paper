from dotenv import load_dotenv
from autorag.evaluator import Evaluator


def run():
    # load environment variables
    load_dotenv()

    # set data path
    qa_data_path = './data/qa.parquet'
    corpus_data_path = './data/corpus.parquet'
    project_dir = './result'
    yaml_path = './config/config.yaml'

    # make evaluator instance
    evaluator = Evaluator(qa_data_path=qa_data_path, corpus_data_path=corpus_data_path, project_dir=project_dir)

    # start trial
    evaluator.start_trial(yaml_path=yaml_path)


if __name__ == '__main__':
    run()
