import wolframalpha
app_id = "Your Wolframalpha API Id."
client = wolframalpha.Client(app_id)
res = client.query(input)
answer = next(res.results).text
print(answer)
