"""genre_results = ['rap', 'classical', 'rock', 'rock', 'country', 'rap',
                 'rock', 'latin', 'country', 'k-pop', 'pop', 'rap',
                 'rock', 'k-pop',  'rap', 'k-pop', 'rock', 'rap', 'latin',
                 'pop', 'pop', 'classical', 'pop', 'country', 'rock',
                 'classical', 'country', 'pop', 'rap', 'latin']

#set
survey_genres = set(genre_results)
print(survey_genres)

survey_abbreviations = {genres[0:3] for genres in genre_results}
print(survey_abbreviations)

#frozenset
top_genres = ["rap", "rock", "pop"]

frozen_top_genres = frozenset(top_genres)
print(frozen_top_genres)

#.add()
song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electric']}

user_tag_1 = 'warm'
user_tag_2 = 'exciting'
user_tag_3 = 'electric'

tag_set = set(song_data["Retro Words"])

tag_set.add(user_tag_1)
tag_set.add(user_tag_2)
tag_set.add(user_tag_3)

song_data["Retro Words"] = tag_set
print(song_data)


#finding elements in set
allowed_tags = ['pop', 'hip-hop', 'rap', 'dance', 'electronic', 'latin', 'indie',
                'alternative rock', 'classical', 'k-pop', 'country', 'rock', 'metal',
                'jazz', 'exciting', 'sad', 'happy', 'upbeat', 'party', 'synth', 'rhythmic',
                'emotional', 'relationship', 'warm', 'guitar', 'fiddle', 'romance', 'chill', 'swing']

song_data_users = {'Retro Words': ['pop', 'explosion', 'hammer', 'bomb', 'warm', 'due', 'writer',
                                   'happy', 'horrible', 'electric', 'mushroom', 'shed']}
tag_set = set(song_data_users["Retro Words"])
bad_tags =  []


for tag in tag_set:
    if tag not in allowed_tags:
        bad_tags.append(tag)

for tag in bad_tags:
    tag_set.discard(tag)"""

#union
"""song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth']}

user_tag_data = {'Lowkey Space': ['party', 'synth', 'fast', 'upbeat'],
                 'Retro Words': ['happy', 'electronic', 'fun', 'exciting'],
                 'Wait For Limit': ['romance', 'chill', 'rap', 'rhythmic'],
                 'Stomping Cue': ['country', 'swing', 'party', 'instrumental']}

new_song_data = {}

for key, value in song_data:
    song_data_set = set(value)
    user_tag_set = set(user_tag_data[key])
    new_song_data[key] = song_data_set | user_tag_set
print(new_song_data)"""

#intersection
"""song_data = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
             'Wait For Limit': ['rap', 'upbeat', 'romance'],
             'Stomping Cue': ['country', 'fiddle', 'party'],
             'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
             'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
             'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
             'Down To Green Hills': ['country', 'relaxing', 'vocal', 'emotional'],
             'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_recent_songs = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat']}

tags_int = set(user_recent_songs["Retro Words"]) & set(user_recent_songs["Lowkey Space"])

recommended_songs = {}

for key, value in song_data.items():
    for tag in value:
        if tag in tags_int:
            if key not in user_recent_songs:
                recommended_songs[key] = value

print(recommended_songs)"""

#difference
"""rec_songs = {}
user_liked_song = {'Back To Art': ['pop', 'sad', 'emotional', 'relationship']}
user_disliked_song = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth']}

tag_diff = set(user_liked_song["Back To Art"]).difference(set(user_disliked_song["Retro Words"]))

for key, val in song_data.items():
    for tag in val:
        if tag in tag_diff:
            if key not in user_liked_song and user_disliked_song:
                rec_songs[key] = val
print(rec_songs)"""

#difference
"""user_song_history = {'Retro Words': ['pop', 'warm', 'happy', 'electronic', 'synth'],
                     'Stomping Cue': ['country', 'fiddle', 'party'],
                     'Back To Art': ['pop', 'sad', 'emotional', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

friend_song_history = {'Lowkey Space': ['electronic', 'dance', 'synth', 'upbeat'],
                     'Blinding Era': ['rap', 'intense', 'moving', 'fast'],
                     'Wait For Limit': ['rap', 'upbeat', 'romance', 'relationship'],
                     'Double Lights': ['electronic', 'chill', 'relaxing', 'piano', 'synth']}

user_tags = set()
for key, value in user_song_history.items():
    user_tags.update(set(value))

friend_tags = set()
for key, value in friend_song_history.items():
    friend_tags.update(set(value))

unique_tags = set(user_tags ^ friend_tags)
print(unique_tags)"""