from panovel import run_pandoc_filter


def latex(self):
    if "odd-page" in self.classes:
        return r"\cleardoublepage"
    return r"\clearpage"


if __name__ == "__main__":
    run_pandoc_filter(["new_page", "new-page"],
                      latex,
                      '<div class="pagebreak"></div>',
                      "\n----\n")
