import pandas


df = pandas.read_csv('wrs_results.csv')

result = df.groupby('Racer Name').agg(
    race_count=('Racer Name','count'),
    total_points=('Points','sum')
).sort_values(by='race_count',ascending=False).reset_index().head(100)

result.columns = ['racer_name','race_count','total_points']
result['total_points'] = result['total_points'].astype(int)

result.to_csv('top_100.csv', index=False)
