from supainsert import SupaInsert

supai = SupaInsert('articles_duplicate')

insert = supai.insert("https://www.gameinformer.com/rss.xml", "f70bd78d-71b0-4fae-9d15-9b321eb0fd75")
print(insert)