#define UNICODE
#include <iostream>
#include <fstream>
#include <random> // for std::mt19937
#include <chrono> // for std::chrono
#include  <iterator>

//generator MT
template<typename Iter, typename RandomGenerator>
Iter select_randomly(Iter start, Iter end, RandomGenerator& g) {
    std::uniform_int_distribution<> dis(0, std::distance(start, end) - 1);
    std::advance(start, dis(g));
    return start;
}

template<typename Iter>
Iter select_randomly(Iter start, Iter end) {
    static std::random_device rd;
    static std::mt19937 gen(rd());
    return select_randomly(start, end, gen);
}

class Node{
public:
	std::vector<Node*> neigh;
	bool checked = false;
	int id;

	Node* goNext(){
		return *select_randomly(neigh.begin(), neigh.end());
	}

	Node(int id){
		this->id = id;
	}
};

class Struktura{
public:
	int n;

	Struktura(int n){
		this -> n = n;
		for(int i = 0; i < n; i++)
			elements.push_back(new Node(i));
	}

	std::vector<Node*> elements;

	virtual Node* start() = 0;

	int walk(){
		for(Node* node : elements)
			node->checked = false;
		Node* node = start();
		int visited = 1;
		long long time = 0;

		while(visited < n){
			node = node->goNext();
			if(node->checked == false){
				node->checked = true;
				visited++;
			}
			time++;

			// std::cout<< node->id<<" ";
		}
		return time;
	}
};

class Klika : public Struktura{
public:
	Klika(int n) : Struktura(n) {
			
		for(int i = 0; i < n; i++)
			for(int j = 0; j < n; j++)
				if(j!=i)
					elements.at(i)->neigh.push_back(elements.at(j));

	}

	Node* start(){
		elements.at(0)->checked = true;
		return elements.at(0);
	}
};

class Sciezka : public Struktura{
public:
	Sciezka(int n) : Struktura(n) {
		elements.at(0)->neigh.push_back(elements.at(1));
		elements.at(n-1)->neigh.push_back(elements.at(n-2));
		for(int i = 1; i < n-1; i++){
			elements.at(i)->neigh.push_back(elements.at(i-1));
			elements.at(i)->neigh.push_back(elements.at(i+1));
		}
	}
};

class SciezkaBok : public Sciezka{
public:
	SciezkaBok(int n) : Sciezka(n){};
	Node* start(){
		elements.at(0)->checked = true;
		return elements.at(0);
	}
};

class SciezkaSrodek : public Sciezka{
public:
	SciezkaSrodek(int n) : Sciezka(n){};
	Node* start(){
		elements.at(n/2)->checked = true;
		return elements.at(n/2);
	}
};

class Drzewo : public Struktura{
public:
	Drzewo(int n) : Struktura(n) {

		elements.at(0)->neigh.push_back(elements.at(1));
		elements.at(0)->neigh.push_back(elements.at(2));
			
		for(int i = 1; i < n; i++){
			elements.at(i)->neigh.push_back(elements.at( (i-1) / 2 ));
			if(i*2+1 < n)
				elements.at(i)->neigh.push_back(elements.at(i*2+1));
			if(i*2+2 < n)
				elements.at(i)->neigh.push_back(elements.at(i*2+2));
		}
	}

	Node* start(){
		elements.at(0)->checked = true;
		return elements.at(0);
	}
};

class Lizak : public Struktura{
public:
	Lizak(int n) : Struktura(n) {
		int connectorId = 2*n/3;
		for(int i = 0; i < connectorId; i++)
			for(int j = 0; j < connectorId; j++)
				if(j!=i)
					elements.at(i)->neigh.push_back(elements.at(j));

		elements.at(connectorId - 1)->neigh.push_back(elements.at(connectorId));
		elements.at(connectorId)->neigh.push_back(elements.at(connectorId - 1));
		elements.at(connectorId)->neigh.push_back(elements.at(connectorId + 1));
		elements.at(n-1)->neigh.push_back(elements.at(n-2));
		for(int i = connectorId + 1; i < n-1; i++){
			elements.at(i)->neigh.push_back(elements.at(i-1));
			elements.at(i)->neigh.push_back(elements.at(i+1));
		}
	}

	Node* start(){
		elements.at(0)->checked = true;
		return elements.at(0);
	}
};

void write(int kmax){
	std::ofstream stream;
	stream.open("results/lizakdwa.txt");					// tutaj

	for (int n = 100; n < 2000; n+=50){
		Struktura* s = new Drzewo(n);					// tutaj
		std::cout<<n<<std::endl;
		for(int k = 0; k < kmax; k++){
			stream<< s->walk() <<" ";
		}
		stream<<std::endl;
		free(s);
	}
	stream.close();
}
int main(){
	write(50);											// tutaj
	std::cout<<"koniec"<<std::endl;
}

/**
 * Tam gdzie jest "tutaj" zmieniamy typy obiektów / nazwy
 * liczba próbek:
 * Drzewo: 100
 * Klika: 100
 * SciezkaBok: 25
 * SciezkaSrodek: 15
 * Lizak: 5 (ponad godzinę!)
 */
