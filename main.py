import os

# Final: not a value, a reaction. When a machine is lost mid-task, the
# deadpan status it blurts is that it is working out where it is again —
# flat, put-upon, and instantly recognisable with no caption needed.
word = "recalculating"

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", ".")
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(word)
