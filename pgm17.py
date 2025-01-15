d={"banana":10,"grape":5,"watermelon":8,"orange":10}
print(d)
r=dict(sorted(d.items()))
print(r)
print("descending")
r=dict(sorted(d.items(),reverse=True))
print(r)
