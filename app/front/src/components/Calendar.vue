<template>
  <div class="calendar">
    <div class="header">
      <button @click="previousWeek">前の週</button>
      <h2>{{ currentWeekRange }}</h2>
      <button @click="nextWeek">次の週</button>
    </div>
    <table>
      <thead>
        <tr>
          <th v-for="day in daysOfWeek" :key="day">{{ day }}</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(week, index) in calendar" :key="index">
          <td v-for="(date, subIndex) in week" :key="subIndex" @click="selectDate(date)">
            {{ date.getDate() }}
          </td>
        </tr>
      </tbody>
    </table>
    <div class="memo">
      <h3>メモ</h3>
      <textarea v-model="selectedDateMemo"></textarea>
    </div>
  </div>
</template>

<script>
export default {
  data() {
    return {
      currentWeek: new Date(), // 現在の週を表すDateオブジェクト
      daysOfWeek: ['日', '月', '火', '水', '木', '金', '土'], // 曜日の配列
      selectedDateMemo: '', // 選択された日付のメモ
    };
  },
  computed: {
    calendar() {
      const weekStart = new Date(this.currentWeek);
      weekStart.setDate(weekStart.getDate() - weekStart.getDay());
      const weekEnd = new Date(this.currentWeek);
      weekEnd.setDate(weekEnd.getDate() + (6 - weekEnd.getDay()));

      const calendar = [];
      let currentDate = new Date(weekStart);

      while (currentDate <= weekEnd) {
        calendar.push(new Date(currentDate));
        currentDate.setDate(currentDate.getDate() + 1);
      }

      return calendar;
    },
    currentWeekRange() {
      const weekStart = new Date(this.currentWeek);
      weekStart.setDate(weekStart.getDate() - weekStart.getDay());
      const weekEnd = new Date(this.currentWeek);
      weekEnd.setDate(weekEnd.getDate() + (6 - weekEnd.getDay()));

      const startDate = weekStart.getDate();
      const startMonth = weekStart.getMonth() + 1;
      const endDate = weekEnd.getDate();
      const endMonth = weekEnd.getMonth() + 1;

      return `${startMonth}/${startDate} - ${endMonth}/${endDate}`;
    },
  },
  methods: {
    previousWeek() {
      this.currentWeek.setDate(this.currentWeek.getDate() - 7);
    },
    nextWeek() {
      this.currentWeek.setDate(this.currentWeek.getDate() + 7);
    },
    selectDate(date) {
      console.log('選択された日付:', date);
    },
  },
};
</script>

<style scoped>
.calendar {
  font-family: Arial, sans-serif;
}

.header {
  display: flex;
  justify-content: space-between;
  align-items: center;
  margin-bottom: 10px;
}

table {
  width: 100%;
  border-collapse: collapse;
}

th,
td {
  border: 1px solid #ccc;
  padding: 5px;
  text-align: center;
  width: 250px; /* セルの幅を調整 */
  height: 120px; /* セルの高さを調整 */
}

td {
  cursor: pointer;
  
}

td:hover {
  background-color: #f5f5f5;
}

.memo {
  margin-top: 20px;
}

textarea {
  width: 100%;
  height: 200px;
  resize: vertical;
}
</style>

<!-- </script> -->
