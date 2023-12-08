class ListMethodExplainer:
    def __init__(self, namensliste):
        self.original_list = namensliste.copy()

    def explain_pop(self):
        namensliste = self.original_list.copy()
        print("pop() removes and returns the last item in the list.")
        if namensliste:
            last_item = namensliste.pop()
            print(f"The last item, which was removed: {last_item}")
        print(f"The list after pop: {namensliste}")

    def explain_pop_i(self, i):
        namensliste = self.original_list.copy()
        if 0 <= i < len(namensliste):
            print(f"pop(i) removes and returns the item at index i (in this case, index {i}).")
            item = namensliste.pop(i)
            print(f"The item at index {i}, which was removed: {item}")
        else:
            print(f"No item at index {i}, so pop(i) cannot be demonstrated.")
        print(f"The list after pop(i): {namensliste}")

    def explain_append(self, x):
        namensliste = self.original_list.copy()
        print(f"append(x) adds an item (x) to the end of the list. Appending: {x}")
        namensliste.append(x)
        print(f"The list after appending: {namensliste}")

    def explain_extend(self, x):
        namensliste = self.original_list.copy()
        print(f"extend(x) extends the list by appending all items from the iterable (x). Extending with: {x}")
        namensliste.extend(x)
        print(f"The list after extending: {namensliste}")

    def explain_remove(self, x):
        namensliste = self.original_list.copy()
        print(f"remove(x) removes the first occurrence of an item (x) from the list. Removing: {x}")
        try:
            namensliste.remove(x)
            print(f"The list after removing: {namensliste}")
        except ValueError:
            print(f"The item {x} was not found in the list and cannot be removed.")

    def explain_index(self, x):
        namensliste = self.original_list.copy()
        print(f"index(x) returns the index of the first occurrence of an item (x). Finding index of: {x}")
        try:
            index = namensliste.index(x)
            print(f"The first occurrence of {x} is at index: {index}")
        except ValueError:
            print(f"The item {x} was not found in the list.")

    def explain_insert(self, i, x):
        namensliste = self.original_list.copy()
        print(f"insert(i, x) inserts an item (x) at a given position (i). Inserting {x} at index {i}")
        namensliste.insert(i, x)
        print(f"The list after insertion: {namensliste}")

    def explain_sort(self):
        namensliste = self.original_list.copy()
        print("sort() sorts the list in place.")
        namensliste.sort()
        print(f"The list after sorting: {namensliste}")

# Example usage:
names = ['Peter', 'Miguel', 'Denis']
explainer = ListMethodExplainer(names)

explainer.explain_pop()
explainer.explain_pop_i(1)  
explainer.explain_append('Thomas')
explainer.explain_extend(['Calvin', 'Sophia'])
explainer.explain_remove('Miguel')  
explainer.explain_index('Peter')     
explainer.explain_insert(1, 'Julia') 
explainer.explain_sort()


# Wenn wir zwei Listen kombinieren möchten verwenden wir extend, begründung: 
# append() erweitert die Liste mit exakt einem Element. Das würde in diesem Fall bedeuten, dass die hinzugefügte Liste
# als 'Liste in der Liste' existieren würde. extend() erweitert die Liste um die Elemente, die im Argument der Funktion gegeben wurden. 
# und würde für jedes Listenelement einen neunen Index zur Liste hinzufügen. 