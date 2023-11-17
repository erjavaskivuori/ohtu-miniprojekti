from entities.citation import Citation

class CitationManager():
    def __init__(self):
        self.all = []

    def add_citation(self, citation :Citation):
        self.all.append(citation)
        
    def return_all_citaions(self):
        return self.all
    
    def print_all(self):
        for citation in self.all:
            print(citation)
    
    def delete_citation(self,citation):
        None

    def search_citation(self,citation):
        None

# if __name__=="__main__":
#     testi = Citation("a","a","a",11)
#     print(testi)