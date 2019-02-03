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

    def get_mono_color_casting_probability(self, colored_cost, colorless_cost, colored_lands, other_lands, sample_size,
                                           successes_in_library=4, library_size=60):
        other_cards = library_size - successes_in_library - colored_lands - other_lands
        cum = 0
        for successes_drawn in range(1, successes_in_library + 1):
            for other_cards_drawn in range(sample_size - successes_drawn - colored_cost - colorless_cost + 1):
                for colored_lands_drawn in range(colored_cost, sample_size - successes_drawn - other_cards_drawn + 1):
                    other_lands_drawn = sample_size - successes_drawn - other_cards_drawn - colored_lands_drawn
                    if successes_drawn + other_cards_drawn + colored_lands_drawn + other_lands_drawn != sample_size:
                        print("error")
                    print(successes_drawn, colored_lands_drawn, other_lands_drawn, other_cards_drawn)
                    a = comb(successes_in_library, successes_drawn, exact=True)
                    b = comb(colored_lands, colored_lands_drawn, exact=True)
                    c = comb(other_lands, other_lands_drawn, exact=True)
                    d = comb(other_cards, other_cards_drawn, exact=True)
                    cum += a * b * c * d
        probability_both = cum / comb(library_size, sample_size, exact=True)
        probability_drawn = self.calc_cum(sample_size=10)
        return probability_both/probability_drawn


if __name__ == "__main__":
    hgc = HyperGeoCalc()
    print(hgc.calc())
    print(hgc.calc_cum())
    print(hgc.get_mono_color_casting_probability(colored_cost=2, colorless_cost=1,
                                                 colored_lands=18, other_lands=8, sample_size=10))

#likelihood you can cast card x by turn y
#do you have the lands?
#do you have the card?
