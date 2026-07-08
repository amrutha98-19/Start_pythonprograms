# copy() -> Returns a copy of the list.
# copy() -> creates a new list with the same elements as the original list.
# Changes made to the copied list do not affect the original list.
flowers=['rose','tulip','daisy','sunflower']
newflowers=flowers.copy()
newflowers.append('marigold')
print("original list:",flowers)
print("copied list:",newflowers)