// modules-list.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-modules-list',
  templateUrl: './modules-list.component.html',
  styleUrls: ['./modules-list.component.css']
})
export class ModulesListComponent {
  modules = [
    {
      name: 'Formation Humaine 1',
      courses: ['LICENCE-GLSI-3511 : Anglais Technique', 'LICENCE-GLSI-3512 : Aspects juridiques et éthique des TIC', "LICENCE-GLSI-3513 : Technique d'expression"]
    },
    {
      name: 'Algorithme et Langages avancés 1',
      courses: ['LICENCE-GLSI-3533 : Programmation Orienté-Objet avancée', 'LICENCE-GLSI-3532 : Langage C', 'LICENCE-GLSI-3531 : Algorithmique et Structures de Données']
    }
  ];
}




