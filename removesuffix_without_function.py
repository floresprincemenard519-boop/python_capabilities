string = "This text should not have a smiley face in the end.  :)"
suffix_to_remove = "  :)"

print(string[:len(string)-len(suffix_to_remove)])