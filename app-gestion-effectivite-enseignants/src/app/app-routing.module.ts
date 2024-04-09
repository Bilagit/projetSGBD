import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { ErrorComponent } from './_utils/error/error.component';
import { AuthGuard } from './_helpers/auth.guard';
import { ProfilEtudiantComponent } from './profil/profil-etudiant/profil-etudiant.component';
import { ProfilEnseignantComponent } from './profil/profil-enseignant/profil-enseignant.component';


const routes: Routes = [
  {
    path: '', loadChildren: () => import('./pulic/pulic.module')
    .then(m => m.PulicModule)
  },
  {path: 'admin', loadChildren: () => import('./admin/admin.module')
    .then(m => m.AdminModule), canActivate:[AuthGuard] 
  },

  {path: 'auth', loadChildren: () => import('./auth/auth.module')
  .then(m => m.AuthModule)
  },

  { path: 'profil-etudiant', component: ProfilEtudiantComponent },
  { path: 'profil-enseignant', component: ProfilEnseignantComponent },

  {path: '**', component: ErrorComponent}
 
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
