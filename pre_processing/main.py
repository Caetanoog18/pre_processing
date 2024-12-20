from tensorflow.python.ops.summary_ops_v2 import graph

from pre_processing.census_database import CensusDatabase
from pre_processing.census_graph import CensusGraph
from pre_processing.pre_processing_database import InconsistentValues, Census
from pre_processing.credit_risk_graph import *
from pre_processing.census_database import *


file_path_credit = "/home/gabriel-caetano/Desktop/Tensorflow/pre_processing/database/credit_data.csv"
file_path_census = "/home/gabriel-caetano/Desktop/Tensorflow/pre_processing/database/census.csv"

# graphs = Graphs(file_path_credit)
# graphs.generate_dynamic_graph("dynamic_1")
# graphs.historian_chart_age("historian_age_1")
#
credit = InconsistentValues(file_path_credit)
credit.inconsistent_values()
#
# inconsistent_values.generate_dynamic_graph("dynamic_1")
# inconsistent_values.historian_chart_age("historian_age_2")
#
credit.missing_values()
#
credit.division_predictors_class()

credit.training_credit_database()
credit.save_variables()

census_database = CensusDatabase(file_path_census)
census_database.statistics_census()
#
# census_graph = CensusGraph(file_path_census)
# census_graph.view_census_data("census_graph_income")
# census_graph.historian()
#
census = Census(file_path_census)
census.division_predictors_class_census()
census.label_encoder()
census.one_hot_encoder()
census.scaling_values()
census.training_census_database()
census.save_variables()

