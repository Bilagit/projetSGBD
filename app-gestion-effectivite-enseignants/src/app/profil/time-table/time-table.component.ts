// timetable.component.ts
import { Component } from '@angular/core';

@Component({
  selector: 'app-timetable',
  templateUrl: './time-table.component.html',
  styleUrls: ['./time-table.component.css']
})
export class TimetableComponent {
  timetable = [
    { date: 'Lundi', course: 'Algorithmique et Structures de Données', teacher: 'Professeur Gaye' },
    { date: 'Mardi', course: 'LICENCE-GLSI-3513 :Anglais Technique ', teacher: 'Mister Wade' },
    { date: 'Mercredi', course: 'Langage C', teacher: 'Mr Toure' },
    { date: 'Jeudi', course: 'POO', teacher: 'Professeur Diop' },
    { date: 'Vendredi', course: 'Recherche Operationnelle', teacher: 'Professeur Ba' },
  ];
}

