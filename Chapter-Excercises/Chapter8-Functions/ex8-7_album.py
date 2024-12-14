def make_album(artist, title, songs=None):
   album = {
      'Artist': artist,
      'Title': title
   }

   if songs:
      album['Songs'] = songs

   return album

fav_musician = make_album('Carti', 'Die Lit')
new_musician = make_album('Lil Uzi Vert', 'Pink Tape')
old_musician = make_album('Kid Cudi', 'Man On The Moon', 12)

print(fav_musician)
print(new_musician)
print(old_musician)