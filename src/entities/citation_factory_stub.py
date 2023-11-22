from citations.citation_factory import CitationFactory
from citations.citation_type import CitationType


if __name__=="__main__":
    print("testi:")
    factory = CitationFactory()
    citation = factory.get_new_citation(CitationType.BOOK)
    print(citation)
    citation.attributes[0].set_value("Tommi")
    print(citation.attributes[0].get_name() + " is now Tommi ")
    print(citation)
    
    #author: 
    #title: 
    #year: 

    #author is now Tommi 
    #author: Tommi
    #title:
    #year:
    
    citation = factory.get_new_citation(CitationType.ARTICLE)
    print(citation)
    #author:
    #title:
    #journaltitle:
    #year:
    
    
