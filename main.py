from methods.save_file import save_file

from methods.filter import filter_results
from engine.data_extractor import df


filtered_df = filter_results(df)

save_file(filtered_df)
