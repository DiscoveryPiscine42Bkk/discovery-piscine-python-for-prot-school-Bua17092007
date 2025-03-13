def find_the_redheads(family):
  return list(filter(lambda name: family[name] == "red", family))
dupont_family = {
  "florian": "red",
  "marie": "blonde",
  "virginie": "brunette",
  "david": "red",
  "franck": "red"
}
print(find_the_redheads(dupont_family))