from scipy.special import comb

class HyperGeoCalc:

    # def __init__(self, library_size=60, num_cards_required=1, sample_size=7, successes_in_library=4):
    #     self.library_size = library_size #N
    #     self.num_cards_required = num_cards_required #x
    #     self.sample_size = sample_size #n
    #     self.successes_in_library = successes_in_library #k

    def calc(self, library_size=60, num_cards_required=1, sample_size=7, successes_in_library=4):
        # h(x; N, n, k) = [ kCx ] [ N-kCn-x ] / [ NCn ]
        a = comb(successes_in_library, num_cards_required, exact=True)
        b = comb(library_size - successes_in_library, sample_size - num_cards_required, exact=True)
        c = comb(library_size, sample_size, exact=True)

        return a*b/c

    def calc_cum(self, library_size=60, num_cards_required=1, sample_size=7, successes_in_library=4):
        cards = num_cards_required
        cumulative_probability = 0
        for i in range(successes_in_library - num_cards_required):
            cumulative_probability += self.calc(library_size, cards, sample_size, successes_in_library)
            cards += 1
        return cumulative_probability


if __name__ == "__main__":
    hgc = HyperGeoCalc()
    print(hgc.calc())
    print(hgc.calc_cum())

#likelihood you can cast card x by turn y
#do you have the lands?
#do you have the card?
