import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ProfilEtudiantComponent } from './profil-etudiant/profil-etudiant.component';
import { ProfilEnseignantComponent } from './profil-enseignant/profil-enseignant.component';
import { ModulesListComponent } from './modules-list/modules-list.component';
import { SyllabusComponent } from './syllabus/syllabus.component';
import { TimetableComponent } from './time-table/time-table.component';


const routes: Routes = [
  //{path: '', redirectTo: 'login', pathMatch: 'full' },

  {path: 'profil', loadChildren: () => import('./profil.module')
      .then(m => m.ProfilModule)
    },

  {path: 'profil-etudiant', component: ProfilEtudiantComponent },

  {path: 'profil-enseignant', component: ProfilEnseignantComponent },

  {path: 'modules-list', component: ModulesListComponent },

  {path: 'timetable', component: TimetableComponent },

  {path: 'syllabus', component: SyllabusComponent }

  
];


@NgModule({
  imports: [RouterModule.forChild(routes)],
  exports: [RouterModule]
})
export class ProfilRoutingModule { }
