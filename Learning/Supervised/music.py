from sklearn.linear_model import LogisticRegression

#input features: pop score, rnb score
X = [
    [8, 2],  # high pop, low rnb
    [7, 3],  # high pop, low rnb
    [2, 8],  # low pop, high rnb
    [3, 7],  # low pop, high rnb
    [9, 1],  # very high pop, very low rnb
    [1, 9],   # very low pop, very high rnb
    [5,6],  # balanced
    [6,5],   # balanced
    [7,7]   # balanced
]
#labels: 1=pop music, 0=rnb music
y = [1, 1, 0, 0, 1, 0, 0, 1, 0]
model = LogisticRegression()

#model learns the relationship between X and y
model.fit(X, y)

# your listening profile
you = [[3, 7]] # low pop score, high rnb score

prediction = model.predict(you)

if prediction[0] == 0:
    print("you like moody pop / rnb")
else:
    print("you like pop")

if prediction[0] == 0:
    recommendations = [
        "tate mcrae – revolving door",
        "the weeknd – die for you",
        "kid laroi – still chose you",
        "zayn – pillowtalk",
        "ariana grande – pov",
        "tate mcrae – uh oh",
        "giveon – heartbreak anniversary",
        "brent faiyaz – dead man walking",
        "sza – snooze",
        "olivia rodrigo – traitor"
    ]
else:
    recommendations = [
        "one direction – you & i",
        "ariana grande – no tears left to cry",
        "taylor swift – style",
        "troye sivan – lucky strike",
        "shawn mendes – mercy",
        "camila cabello – used to this",
        "selena gomez – who says",
        "justin bieber – company",
        "charlie puth – attention",
        "halsey – without me"
    ]

for song in recommendations:
    print(song)

#how this is supervised learning
#inputs (x): listening features derived from artist history
#outputs (y): music preference labels
#the model learns from labeled user data
#predictions are made for a new user
#recommendations are generated based on predicted preference