import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProfilRoutingModule } from './profil-routing.module';
import { ProfilEtudiantComponent } from './profil-etudiant/profil-etudiant.component';
import { ProfilEnseignantComponent } from './profil-enseignant/profil-enseignant.component';
import { ModulesListComponent } from './modules-list/modules-list.component';
import { TimetableComponent } from './time-table/time-table.component';
import { SyllabusComponent } from './syllabus/syllabus.component';


@NgModule({
  declarations: [
    ProfilEtudiantComponent,
    ProfilEnseignantComponent,
    ModulesListComponent,
    TimetableComponent,
    SyllabusComponent
  ],
  imports: [
    CommonModule,
    ProfilRoutingModule,
  ]
})
export class ProfilModule { }
