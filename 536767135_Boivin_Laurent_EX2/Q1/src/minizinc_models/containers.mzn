%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Modele des conteneurs
%% Auteur: Michael Morin

% Ce modele permet de resoudre le probleme de positionnement des conteneurs.
% La grille de conteneurs est modelisee comme un graphe.
% Chaque "Node" represente une cellule.
% Chaque "Edge" represente un lien entre deux cellules adjacentes.
% Dans le graphe de la grille, une cellule est liee a ses 4 voisins:
%  - au nord
%  - au sud
%  - a l'est
%  - a l'ouest
%
% VoidNodes represente les cellules occupees: celle sur lesquelles on ne peut
% pas placer de conteneurs.
%
% Attention, plusieurs parametres sont calcules dans le fichier .mzn a partir
% des donnees du fichier .dzn ou de celle passees en parametres.
% Les seules donnees qu'a besoin le modele sont:
%  - HEIGHT
%  - WIDTH
%  - VoidNodes
% Le reste est calcule.


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Parametres en entree
int: HEIGHT;
int: WIDTH;
set of int: VoidNodes; % Cellules occupees


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Parametres calcules

% Ensemble des noeuds (cellules)
set of int: Nodes = 1..(HEIGHT * WIDTH);

% Nombre de "liens" entre les cellules
int: NBEDGES = 2 * WIDTH * HEIGHT - HEIGHT - WIDTH;

% n1 et n2 forment une liste d'aretes entre les noeuds de la grile
% (liens entre les cellules directement adjacentes).
% La ieme paire est (n1[i], n2[i]) de sorte que n1[i] represente son
% premier element et n2[i] sont second element.
array[1..NBEDGES] of int: 
  n1 = [x1 | x1, x2 in Nodes where x1 < x2 
                                   /\ ((x2 = x1 + 1 
                                        /\ x2 mod WIDTH != 1) 
                                       \/ x2 = x1 + WIDTH) 
                                   /\ x2 <= HEIGHT * WIDTH 
       ];
array[1..NBEDGES] of int: 
  n2 = [x2 | x1, x2 in Nodes where x1 < x2 
                                   /\ ((x2 = x1 + 1 
                                        /\ x2 mod WIDTH != 1) 
                                       \/ x2 = x1 + WIDTH) 
                                   /\ x2 <= HEIGHT * WIDTH 
       ];
       

%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Variables

% vEdge est un vecteur de booleens qui represente le fait de selectionner une
% arete dans le modele.
% Dans cette modelisation, selectionner une arete revient a position un 
% conteneur sur les deux cellules adjacentes a l'arete.
array[1..NBEDGES] of var bool: vEdge;

% Variable qui contient la valeur de fonction objectif:
var int: Z;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Contraintes

% Si on selectionne une arete, cette arete ne partage aucun noeud avec une
% arete differente deja selectionnee.
constraint forall(e in 1..NBEDGES)(
  vEdge[e] = true 
  -> 
  forall(k in 1..NBEDGES diff {e})(
    (n1[k] == n1[e] \/ n2[k] == n2[e] \/ n1[k] == n2[e] \/ n2[k] == n1[e]) 
    -> 
    vEdge[k] = false
  )
);

% Si on selectionne une arete, les noeud de l'arete ne sont pas dans 
% VoidNodes.
constraint forall(e in 1..NBEDGES)(
  vEdge[e] = true
  ->
  not(n1[e] in VoidNodes \/ n2[e] in VoidNodes)
);

% Calcul de l'objectif
constraint(
  Z = sum(e in 1..NBEDGES)(vEdge[e])
);


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Resolution

% On resout en maximisant Z:
solve maximize Z;


%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
%% Affichage console

% Toutes les paires de positions sélectionnées de conteneurs sont affichées
% à console:
output
[ 
  concat([
      if fix(vEdge[e]) == true then
        show(n1[e]) 
        ++ 
        " " 
        ++ 
        show(n2[e]) 
        ++ 
        "|" 
      else
        ""
      endif
    | e in 1..NBEDGES
    ])
];

%% Fin du fichier
%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%