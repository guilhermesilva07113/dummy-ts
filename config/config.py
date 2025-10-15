import os

# %%
# PACKAGE DIR
PACKAGE_DIR = os.path.dirname(os.path.dirname(__file__))
# %%
# DATA DIR
DATA_DIR_PATH = os.path.join(PACKAGE_DIR, "data")
# FOLDERs
DATA_RAW_PATH = os.path.join(DATA_DIR_PATH, "01_raw")
DATA_INTERMEDIATE_PATH = os.path.join(DATA_DIR_PATH, "02_intermediate")
DATA_FEATURE_PATH = os.path.join(DATA_DIR_PATH, "04_feature")
DATA_INPUT_PATH = os.path.join(DATA_DIR_PATH, "05_model_input")
DATA_MODELS_PATH = os.path.join(DATA_DIR_PATH, "06_models")
DATA_OUTPUT_PATH = os.path.join(DATA_DIR_PATH, "07_model_output")
DATA_REPORTING_PATH = os.path.join(DATA_DIR_PATH, "08_reporting")
DATA_PRODUCTION_PATH = os.path.join(DATA_DIR_PATH, "09_production")
DATA_EXPERIMENTS_PATH = os.path.join(DATA_DIR_PATH, "09_save_experiments")
DATA_OUTPUT_API_PATH = os.path.join(DATA_DIR_PATH, "10_model_output")
# FILES
DATA_TARGET_RAW = os.path.join(DATA_RAW_PATH, "canvas_dataset_ANP_volumeMensalPorUF.csv")
DATA_TARGET_INPUT = os.path.join(DATA_INPUT_PATH, "dados_input_model.csv")