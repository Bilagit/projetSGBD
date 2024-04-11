import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { HomeComponent } from './home/home.component';
import { PlayoutComponent } from './playout/playout.component';
import { GestionEnseignantComponent } from './gestion-enseignant/gestion-enseignant.component';
import { ProfilEtudiantComponent } from '../profil/profil-etudiant/profil-etudiant.component';
import { ProfilEnseignantComponent } from '../profil/profil-enseignant/profil-enseignant.component';

const routes: Routes = [
  {path: '', component: PlayoutComponent, children: [
    {path: '', redirectTo: 'home', pathMatch: 'full'},
    {path: 'home', component: HomeComponent },
    {path: 'GestionEnseignant', component: GestionEnseignantComponent },
    {path: 'profil/profil-etudiant', component: ProfilEtudiantComponent },

    {path: 'profil/profil-enseignant', component: ProfilEnseignantComponent }
  ]}
  
];

@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class PublicRoutingModule { }
