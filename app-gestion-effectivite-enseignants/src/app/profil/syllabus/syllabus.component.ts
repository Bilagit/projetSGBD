// syllabus.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-syllabus',
  templateUrl: './syllabus.component.html',
  styleUrls: ['./syllabus.component.css']
})
export class SyllabusComponent {
  syllabus = [
    {
      course: 'Langage C',
      content: `Le cours de Langage C couvrira les concepts de base de la programmation en C, y compris :
      - Les types de données et les variables
      - Les opérateurs arithmétiques, logiques et de comparaison
      - Les structures de contrôle comme les boucles et les instructions conditionnelles
      - Les tableaux et les chaînes de caractères
      - Les fonctions et les pointeurs
      - La gestion de la mémoire et les structures de données de base
      - Les fichiers et les entrées/sorties`
    },
    {
      course: 'Algorithmes',
      content: `Le cours d'Algorithmes couvrira les principaux algorithmes et structures de données, y compris :
      - Recherche séquentielle et binaire
      - Triage (Tri à bulles, Tri par sélection, Tri par insertion, Tri fusion, etc.)
      - Recherche et parcours de graphes
      - Arbres binaires et parcours d'arbres
      - Complexité algorithmique et notation O(n)`
    },
    {
      course: 'Anglais',
      content: `Le cours d'Anglais abordera les compétences linguistiques nécessaires à la communication en anglais, y compris :
      - La grammaire et la syntaxe
      - Le vocabulaire général et spécialisé
      - La compréhension écrite et orale
      - L'expression écrite et orale
      - La culture et la civilisation anglophones`
    },
    {
      course: 'Programmation Orientée Objet (POO)',
      content: `Le cours de POO couvrira les concepts de base de la programmation orientée objet, y compris :
      - Les classes et les objets
      - L'encapsulation et l'abstraction
      - L'héritage et le polymorphisme
      - Les interfaces et les classes abstraites
      - La gestion de la mémoire et la réutilisation du code`
    },
    {
      course: 'Systèmes de Gestion de Bases de Données (SGBD)',
      content: `Le cours de SGBD traitera des principes fondamentaux des systèmes de gestion de bases de données, y compris :
      - Modélisation des données (Modèle entité-association, Modèle relationnel)
      - Langage de requête SQL (Structured Query Language)
      - Conception de bases de données relationnelles
      - Fonctionnalités avancées des SGBD relationnels
      - Sécurité et intégrité des données`
    },
    {
      course: 'Systèmes Embarqués (SE)',
      content: `Le cours de Systèmes Embarqués portera sur la conception et la programmation des systèmes embarqués, y compris :
      - Architecture matérielle des systèmes embarqués
      - Systèmes d'exploitation temps réel
      - Interfaces homme-machine (IHM) et entrées/sorties
      - Gestion de l'énergie et des ressources
      - Développement logiciel embarqué`
    }
  ];
}


