with open("../../xab.txt") as xab:
    xab_text = xab.readlines()
    # Iterate through cleaned.pantun
    with open("cleaned.pantun") as c:
        cleaned = c.readlines()
        lines = []
        new_xab_text = []
        where_to_slice = 0
        for i, line in enumerate(xab_text):
            if line == "===\n":
                continue
            # If `line` is in `cleaned`, otherwise ignore
            if line in cleaned and xab_text[i-1] == "===\n" and xab_text[i+1] == "===\n":
                print(f"line {i}: {xab_text[i]}")
                lines.append(line)
                # Split text content list at index
                xab1 = xab_text[where_to_slice:i+1]
                # Update the `where_to_slice`
                where_to_slice = i+1
                # Get index of `line` in `cleaned`
                cleaned_idx = cleaned.index(line)
                # Find where's the next delimiter (===) after `line` in `cleaned`
                delimiter_idx = 0
                for j in range(cleaned_idx+1, len(cleaned)):
                    if cleaned[j] == "===\n":
                        delimiter_idx = j
                        break
                # Fill in the gaps
                xab1 += cleaned[cleaned_idx+1:delimiter_idx+1]
                new_xab_text += xab1
        # Save to a new file
        with open("filled-in.txt", "w") as w:
            w.writelines(new_xab_text)
        with open("lines.txt", "a") as ls:
            for ln in lines:
                ls.write(ln)
                ls.write('\n')
