
# remove() -> Removes the first matching value from the list.
# pop() -> Removes and returns an item at the specified index.If no index is given, it removes and returns the last item.
# clear() -> Removes all items from the list.

flowers=['rose','jasmin','lotus','lily']
# remove()
flowers.remove('lotus')
print("Remove:",flowers)

# pop()

flowers.pop(2)
print("pop:",flowers)

#clear()
flowers.clear()
print("clear:",flowers)