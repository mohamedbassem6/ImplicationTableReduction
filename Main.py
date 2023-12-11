from tables import StateTable

table = StateTable()

# Test Case: https://slideplayer.com/slide/5135476/

table.add([ord('b') - ord('a'), ord('c') - ord('a')], [0, 0])
table.add([ord('d') - ord('a'), ord('e') - ord('a')], [0, 0])
table.add([ord('f') - ord('a'), ord('g') - ord('a')], [0, 0])
table.add([ord('h') - ord('a'), ord('i') - ord('a')], [0, 0])
table.add([ord('j') - ord('a'), ord('k') - ord('a')], [0, 0])
table.add([ord('l') - ord('a'), ord('m') - ord('a')], [0, 0])
table.add([ord('n') - ord('a'), ord('o') - ord('a')], [0, 0])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 1])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 1])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])
table.add([ord('a') - ord('a'), ord('a') - ord('a')], [0, 0])

print("BEFORE ROW MATCHING:")
table.print_table()

table.row_match()

print("AFTER ROW MATCHING:")
table.print_table()
