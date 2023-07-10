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
    </div>
    <div class="memo-section">
      <div class="memo-grid">
        <div v-for="row in 7" :key="row" class="memo-row">
          <div v-for="col in 2" :key="col" class="memo-cell">
            <textarea v-model="memoGrid[(row - 1) * 7 + col - 1]" @blur="saveMemo(row, col)"></textarea>
          </div>
        </div>
      </div>
    </div>
  </template>
  
  <script>
  export default {
    data() {
      return {
        currentWeek: new Date(),
        daysOfWeek: ['日', '月', '火', '水', '木', '金', '土'],
        selectedDateMemo: '',
        memoGrid: ['', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', '', ''],
        monthCalendar: [], // 追加
      };
    },
    mounted() {
    // ページがロードされた時にmonthCalendarを取得
      this.getMonthCalendar();
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
    watch: {
      currentWeek() {
        this.$nextTick(() => {
          this.updateCurrentWeekRange();
        });
      },
    },
    methods: {
      previousWeek() {
        const nextWeek = new Date(this.currentWeek);
        nextWeek.setDate(nextWeek.getDate() - 7);
        this.currentWeek = nextWeek;
      },
      nextWeek() {
        const nextWeek = new Date(this.currentWeek);
        nextWeek.setDate(nextWeek.getDate() + 7);
        this.currentWeek = nextWeek;
      },
      selectDate(date) {
        console.log('選択された日付:', date);
        this.selectedDateMemo = this.findMemo(date); // 既存のメモを表示
  
        // TODOリストを更新
        const selectedTodo = this.todos.find((todo) => todo.date.getTime() === date.getTime());
        if (selectedTodo) {
          this.selectedDateMemo = selectedTodo.memo;
        } else {
          this.selectedDateMemo = '';
        }
      },
  
      addTodo() {
        const date = this.calendar.find((week) => week.includes(this.selectedDate)).find((d) => d.getTime() === this.selectedDate.getTime());
        if (date) {
          const existingTodoIndex = this.todos.findIndex((todo) => todo.date.getTime() === date.getTime());
          if (existingTodoIndex !== -1) {
            // 既存のTODOがある場合は更新
            this.todos[existingTodoIndex].memo = this.selectedDateMemo;
          } else {
            // 新規のTODOを追加
            this.todos.push({ date: date, memo: this.selectedDateMemo });
          }
        }
      },
  
      findMemo(date) {
        const selectedTodo = this.todos.find((todo) => todo.date.getTime() === date.getTime());
        return selectedTodo ? selectedTodo.memo : '';
      },
  
      saveMemo(row, col) {
        const index = (row - 1) * 2 + col - 1;
        const memo = this.memoGrid[index];
        // メモの保存処理を実行する
        console.log(`Saved memo for row ${row}, col ${col}: ${memo}`);
      },
    },
  };
  </script>
  
  <style scoped>
  
  button{
    margin: 0 230px;
    padding:10px 15px;
    font-size: 20px;
    border: none;
    cursor: pointer;
  }
  
  h2{
    font-size: 40px;
  }
  .memo-section {
    display: flex;
    flex-direction: column;
    align-items: center;
  }
  .memo-grid {
    display: grid;
    grid-template-columns: repeat(7, 1fr);
    grid-gap: 10px;
    margin-top: 20px;
    position: relative;
  }
  
  .memo-grid::before {
    content: "";
    position: absolute;
    top: 50%;
    left: 0;
    right: 0;
    border-top: 1px solid #ccc;
  }
  
  .memo-cell {
    /* border: 1px solid #ccc; */
    border-left: 1px solid #ccc; /* 左側の線を追加 */
    border-right: 1px solid #ccc; /* 右側の線を追加 */
    padding: 5px;
    display: flex;
    justify-content: center;
    align-items: center;
  }
  
  .memo-row {
    position: relative;
  }
  
  .calendar {
    padding: 0px 190px;
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
    border-left: 1px solid #ccc; /* 左側の線を追加 */
    border-right: 1px solid #ccc; /* 右側の線を追加 */
    padding: 5px;
    text-align: center;
    width: 250px;
    height: 120px;
  }
  
  td {
    cursor: pointer;
    
  }
  
  td:hover {
    background-color: #f5f5f5;
  }
  
  textarea {
    width: 100%;
    height: 200px;
    resize: none;
    border: none;
  }
  </style>