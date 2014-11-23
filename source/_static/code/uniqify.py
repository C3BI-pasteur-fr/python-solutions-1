def uniqify(l):
    uniq = []
    for item in l:
       if item not in uniq:
          uniq.append(item)
    return (uniq)