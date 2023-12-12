from tables import StateTable, ImplicationTable

s_table = StateTable()

# Test Case: https://slideplayer.com/slide/5135476/

# s_table.add([ord('b') - ord('a'), ord('c') - ord('a')], [0, 0])
# s_table.add([ord('d') - ord('a'), ord('e') - ord('a')], [0, 0])
# s_table.add([ord('f') - ord('a'), ord('g') - ord('a')], [0, 0])
# s_table.add([ord('h') - ord('a'), ord('i') - ord('a')], [0, 0])
# s_table.add([ord('j') - ord('a'), ord('k') - ord('a')], [0, 0])
# s_table.add([ord('l') - ord('a'), ord('m') - ord('a')], [0, 0])
# s_table.add([ord('n') - ord('a'), ord('o') - ord('a')], [0, 0])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 1])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 1])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
# s_table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])

# s_table.add([ord('d') - ord('a'), ord('c') - ord('a')], [0])
# s_table.add([ord('f') - ord('a'), ord('h') - ord('a')], [0])
# s_table.add([ord('e') - ord('a'), ord('d') - ord('a')], [1])
# s_table.add([ord('a') - ord('a'), ord('e') - ord('a')], [0])
# s_table.add([ord('c') - ord('a'), ord('a') - ord('a')], [1])
# s_table.add([ord('f') - ord('a'), ord('b') - ord('a')], [1])
# s_table.add([ord('c') - ord('a'), ord('h') - ord('a')], [0])
# s_table.add([ord('b') - ord('a'), ord('g') - ord('a')], [1])

# Test Case: Magdy

s_table.add([ord('e') - ord('a'), ord('e') - ord('a')], [1])
s_table.add([ord('c') - ord('a'), ord('e') - ord('a')], [1])
s_table.add([ord('i') - ord('a'), ord('h') - ord('a')], [0])
s_table.add([ord('h') - ord('a'), ord('a') - ord('a')], [1])
s_table.add([ord('i') - ord('a'), ord('f') - ord('a')], [0])
s_table.add([ord('e') - ord('a'), ord('g') - ord('a')], [0])
s_table.add([ord('h') - ord('a'), ord('b') - ord('a')], [1])
s_table.add([ord('c') - ord('a'), ord('d') - ord('a')], [0])
s_table.add([ord('f') - ord('a'), ord('b') - ord('a')], [1])

# s_table.add([ord('h') - ord('a'), ord('c') - ord('a')], [1, 0])
# s_table.add([ord('c') - ord('a'), ord('d') - ord('a')], [0, 1])
# s_table.add([ord('h') - ord('a'), ord('b') - ord('a')], [0, 0])
# s_table.add([ord('f') - ord('a'), ord('h') - ord('a')], [0, 0])
# s_table.add([ord('c') - ord('a'), ord('f') - ord('a')], [0, 1])
# s_table.add([ord('f') - ord('a'), ord('g') - ord('a')], [0, 0])
# s_table.add([ord('g') - ord('a'), ord('c') - ord('a')], [1, 0])
# s_table.add([ord('a') - ord('a'), ord('c') - ord('a')], [1, 0])


print("BEFORE ROW MATCHING:")
s_table.print_table()

s_table.row_match()

print("AFTER ROW MATCHING:")
s_table.print_table()

i_table = ImplicationTable(s_table)

print("IMPLICATION TABLE:")
i_table.print_table()

i_table.imply()

print("IMPLICATION TABLE AFTER REDUCTION:")
i_table.print_table()
