# prmu2019alcon

これはPRMUアルコン2019をcodalabでセットアップしたときの記録です．

# how to

必要事項をかく．

make

bundle.zipをcodalabにアップロード

Editで以下を修正
- Allow teams
- Enable forums
- Anonymous leaderboard
- uncheck: Organizers need to approve the new teams
- （しない：Leaderboard ModeをHideにする）
- Filesページとterms and conditionsページを削除
- Hide Top Three Leaderboardにチェック
- Hide Chartにチェック


詳細は
https://github.com/codalab/codalab-competitions/wiki/Organizer_Codalab-competition-YAML-definition-language


コンペ終了後
- Disallow leaderboard modifyingにチェック
- Force submission to leaderboardにチェック
- Anonymous leaderboardのチェックはずす
- 以下各phaseで
 - Leaderboard ModeをDefaultにする
 - Phase never endsのチェックはずす
 - If submission beats old score, put submission on leaderboardのチェックはずす
 - test-devのmax sumissionを9999にする

