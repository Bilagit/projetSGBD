import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

import { ProfilRoutingModule } from './profil-routing.module';
import { ProfilEtudiantComponent } from './profil-etudiant/profil-etudiant.component';
import { ProfilEnseignantComponent } from './profil-enseignant/profil-enseignant.component';


@NgModule({
  declarations: [
    ProfilEtudiantComponent,
    ProfilEnseignantComponent
  ],
  imports: [
    CommonModule,
    ProfilRoutingModule
  ]
})
export class ProfilModule { }
